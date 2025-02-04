package hexageeks.daftar.models;

import java.util.Date;

import hexageeks.daftar.utils.StorageUtils;

import static hexageeks.daftar.backend.ServerConfig.host;

public class StorageItem {
    private final String id;
    private final String fileExtension;
    private final StorageUtils.FileType fileType;
    private final String fileName;
    private final String fileDescription;
    private final String visibility;
    private final String creatorId;
    private final Date timestamp;

    public StorageItem(String id, String fileExtension, StorageUtils.FileType fileType, String fileName, String fileDescription,
                       String visibility, String creatorId, Date timestamp) {

        this.id = id;
        this.fileExtension = fileExtension;
        this.fileType = fileType;
        this.fileName = fileName;
        this.fileDescription = fileDescription;
        this.visibility = visibility;
        this.creatorId = creatorId;
        this.timestamp = timestamp;
    }

    public String getId() {
        return id;
    }

    public String getFileName() {
        return fileName;
    }

    public String getFileDescription() {
        return fileDescription;
    }

    public String getFileUrl() {
        return host + "/storage/" + id + "?download";
    }

    public String getFileExtension() { return fileExtension; }

    public StorageUtils.FileType getFileType() { return fileType; }

    public String getVisibility() {
        return visibility;
    }

    public String getCreatorId() {
        return creatorId;
    }

    public Date getTimestamp() {
        return timestamp;
    }
}
